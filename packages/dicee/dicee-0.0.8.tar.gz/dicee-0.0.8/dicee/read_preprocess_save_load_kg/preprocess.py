import pandas as pd
import polars as pl
from .util import create_recipriocal_triples, timeit, index_triples_with_pandas, dataset_sanity_checking
from dicee.static_funcs import numpy_data_type_changer
from .util import get_er_vocab, get_re_vocab, get_ee_vocab, create_constraints
import numpy as np
import concurrent


class PreprocessKG:
    """ Preprocess the data in memory """

    def __init__(self, kg):
        self.kg = kg

    def start(self) -> None:
        """
        Preprocess train, valid and test datasets stored in knowledge graph instance

        Parameter
        ---------

        Returns
        -------
        None
        """
        # Before preprocessing
        if self.kg.byte_pair_encoding:
            self.preprocess_with_byte_pair_encoding()
        elif self.kg.backend == "polars":
            self.preprocess_with_polars()
        elif self.kg.backend in ["pandas", "rdflib"]:
            self.preprocess_with_pandas()
        else:
            raise KeyError(f'{self.kg.backend} not found')

        if self.kg.eval_model:
            if self.kg.byte_pair_encoding:
                data = []
                data.extend(self.kg.train_set)
                if self.kg.valid_set is not None:
                    data.extend(self.kg.valid_set)
                if self.kg.test_set is not None:
                    data.extend(self.kg.test_set)
                self.kg.max_length_subword_tokens = len(data[0][0])
            else:
                if isinstance(self.kg.valid_set, np.ndarray) and isinstance(self.kg.test_set, np.ndarray):
                    data = np.concatenate([self.kg.train_set, self.kg.valid_set, self.kg.test_set])
                else:
                    data = self.kg.train_set
            """
            self.er_vocab = get_er_vocab(data, self.path_for_serialization + '/er_vocab.p')
            self.re_vocab = get_re_vocab(data, self.path_for_serialization + '/re_vocab.p')
            self.ee_vocab = get_ee_vocab(data, self.path_for_serialization + '/ee_vocab.p')
            if self.byte_pair_encoding is False:
                self.constraints = create_constraints(self.train_set,
                                                      self.path_for_serialization + '/constraints.p')
            """

            print('Submit er-vocab, re-vocab, and ee-vocab via  ProcessPoolExecutor...')
            # We need to benchmark the benefits of using futures  ?
            executor = concurrent.futures.ProcessPoolExecutor()
            self.kg.er_vocab = executor.submit(get_er_vocab, data, self.kg.path_for_serialization + '/er_vocab.p')
            self.kg.re_vocab = executor.submit(get_re_vocab, data, self.kg.path_for_serialization + '/re_vocab.p')
            self.kg.ee_vocab = executor.submit(get_ee_vocab, data, self.kg.path_for_serialization + '/ee_vocab.p')

            self.kg.constraints = executor.submit(create_constraints, self.kg.train_set,
                                                  self.kg.path_for_serialization + '/constraints.p')
            self.kg.domain_constraints_per_rel, self.kg.range_constraints_per_rel = None, None

        if self.kg.max_length_subword_tokens is None and self.kg.byte_pair_encoding:
            assert isinstance(self.kg.train_set, list)
            assert isinstance(self.kg.train_set[0], tuple)
            assert isinstance(self.kg.train_set[0][0], tuple)
            self.kg.max_length_subword_tokens = len(self.kg.train_set[0][0])

        """
        @TODO: Temporarily ignored
        print('Finding suitable integer type for the index...')
        self.kg.train_set = numpy_data_type_changer(self.kg.train_set,
                                                    num=max(self.kg.num_entities, self.kg.num_relations))
        if self.kg.valid_set is not None:
            self.kg.valid_set = numpy_data_type_changer(self.kg.valid_set,
                                                        num=max(self.kg.num_entities, self.kg.num_relations))
        if self.kg.test_set is not None:
            self.kg.test_set = numpy_data_type_changer(self.kg.test_set,
                                                       num=max(self.kg.num_entities, self.kg.num_relations))
        """

    @timeit
    def preprocess_with_byte_pair_encoding(self) -> None:
        """
        Transform three-dimensional train_set, valid_set, and test_set pandas dataframes
        containing triples (h,r,t) in string representations into respective dataframes containing
        sequences of sub-word units representation of triples
        ([1,2,222,222,222], [11,43, 1026, 222, 222], [8, 222,222,222,222]). where 222 denotes the index of a dummy
        sub-word to represent a triple into fixed shape/dimension.


        Returns
        -------

        """
        assert isinstance(self.kg.train_set, pd.DataFrame)
        self.kg.train_set = list(
            self.kg.train_set.map(lambda x: tuple(self.kg.enc.encode(x))).itertuples(index=False, name=None))
        assert isinstance(self.kg.train_set, list)
        assert isinstance(self.kg.train_set[0], tuple)
        assert len(self.kg.train_set[0]) == 3
        assert isinstance(self.kg.train_set[0][0], tuple)
        assert isinstance(self.kg.train_set[0][0][0], int)

        temp = []
        temp.extend(self.kg.train_set)
        if self.kg.valid_set is not None:
            self.kg.valid_set = list(
                self.kg.valid_set.map(lambda x: tuple(self.kg.enc.encode(x))).itertuples(index=False, name=None))
            temp.extend(self.kg.valid_set)

        if self.kg.test_set is not None:
            self.kg.test_set = list(
                self.kg.test_set.map(lambda x: tuple(self.kg.enc.encode(x))).itertuples(index=False, name=None))
            temp.extend(self.kg.test_set)
        tokens = set()
        bpe_subwords_to_shaped_bpe_entities = dict()
        max_length_subword_tokens = 0

        # Iterate over all triples to find the longest sequence.
        for i in temp:
            max_token_length_per_triple = max(len(i[0]), len(i[1]), len(i[2]))
            if max_token_length_per_triple > max_length_subword_tokens:
                max_length_subword_tokens = max_token_length_per_triple

        print("Longest sequence of subwords of an entity or relation is ", max_length_subword_tokens)
        for i, (s, p, o) in enumerate(self.kg.train_set):
            if len(s) < max_length_subword_tokens:
                s_encoded = s + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(s)))
            else:
                s_encoded = s

            if len(p) < max_length_subword_tokens:
                p_encoded = p + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(p)))
            else:
                p_encoded = p

            if len(o) < max_length_subword_tokens:
                o_encoded = o + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(o)))
            else:
                o_encoded = o

            tokens.add(s_encoded)
            tokens.add(p_encoded)
            tokens.add(o_encoded)
            bpe_subwords_to_shaped_bpe_entities[o] = o_encoded
            bpe_subwords_to_shaped_bpe_entities[s] = s_encoded
            self.kg.train_set[i] = (s_encoded, p_encoded, o_encoded)

        if self.kg.valid_set is not None:
            for i, (s, p, o) in enumerate(self.kg.valid_set):
                if len(s) < max_length_subword_tokens:
                    s_encoded = s + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(s)))
                else:
                    s_encoded = s
                if len(p) < max_length_subword_tokens:
                    p_encoded = p + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(p)))
                else:
                    p_encoded = p
                if len(o) < max_length_subword_tokens:
                    o_encoded = o + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(o)))
                else:
                    o_encoded = o
                tokens.add(s_encoded)
                tokens.add(p_encoded)
                tokens.add(o_encoded)
                bpe_subwords_to_shaped_bpe_entities[o] = o_encoded
                bpe_subwords_to_shaped_bpe_entities[s] = s_encoded
                self.kg.valid_set[i] = (s_encoded, p_encoded, o_encoded)

        if self.kg.test_set is not None:
            for i, (s, p, o) in enumerate(self.kg.test_set):
                if len(s) < max_length_subword_tokens:
                    s_encoded = s + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(s)))
                else:
                    s_encoded = s
                if len(p) < max_length_subword_tokens:
                    p_encoded = p + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(p)))
                else:
                    p_encoded = p
                if len(o) < max_length_subword_tokens:
                    o_encoded = o + tuple(self.kg.dummy_id for _ in range(max_length_subword_tokens - len(o)))
                else:
                    o_encoded = o
                tokens.add(s_encoded)
                tokens.add(p_encoded)
                tokens.add(o_encoded)

                bpe_subwords_to_shaped_bpe_entities[o] = o_encoded
                bpe_subwords_to_shaped_bpe_entities[s] = s_encoded

                self.kg.test_set[i] = (s_encoded, p_encoded, o_encoded)

        self.kg.ordered_bpe_entities = [(self.kg.enc.decode(k), k, v) for k, v in
                                        bpe_subwords_to_shaped_bpe_entities.items()]

    @timeit
    def preprocess_with_pandas(self) -> None:
        """
        Preprocess train, valid and test datasets stored in knowledge graph instance with pandas

        (1) Add recipriocal or noisy triples
        (2) Construct vocabulary
        (3) Index datasets

        Parameter
        ---------

        Returns
        -------
        None
        """
        # (1)  Add recipriocal or noisy triples.
        self.apply_reciprical_or_noise()

        # (2) Construct integer indexing for entities and relations.
        self.sequential_vocabulary_construction()
        self.kg.num_entities, self.kg.num_relations = len(self.kg.entity_to_idx), len(self.kg.relation_to_idx)

        # (3) Index datasets
        self.kg.train_set = index_triples_with_pandas(self.kg.train_set,
                                                      self.kg.entity_to_idx,
                                                      self.kg.relation_to_idx)
        assert isinstance(self.kg.train_set, pd.core.frame.DataFrame)
        self.kg.train_set = self.kg.train_set.values
        self.kg.train_set = numpy_data_type_changer(self.kg.train_set,
                                                    num=max(self.kg.num_entities, self.kg.num_relations))
        dataset_sanity_checking(self.kg.train_set, self.kg.num_entities, self.kg.num_relations)
        if self.kg.valid_set is not None:
            self.kg.valid_set = index_triples_with_pandas(self.kg.valid_set, self.kg.entity_to_idx,
                                                          self.kg.relation_to_idx)
            self.kg.valid_set = self.kg.valid_set.values
            dataset_sanity_checking(self.kg.valid_set, self.kg.num_entities, self.kg.num_relations)
            self.kg.valid_set = numpy_data_type_changer(self.kg.valid_set,
                                                        num=max(self.kg.num_entities, self.kg.num_relations))

        if self.kg.test_set is not None:
            self.kg.test_set = index_triples_with_pandas(self.kg.test_set, self.kg.entity_to_idx,
                                                         self.kg.relation_to_idx)
            # To numpy
            self.kg.test_set = self.kg.test_set.values
            dataset_sanity_checking(self.kg.test_set, self.kg.num_entities, self.kg.num_relations)
            self.kg.test_set = numpy_data_type_changer(self.kg.test_set,
                                                       num=max(self.kg.num_entities, self.kg.num_relations))

    @timeit
    def preprocess_with_polars(self) -> None:
        print(f'*** Preprocessing Train Data:{self.kg.train_set.shape} with Polars ***')
        # (1) Add reciprocal triples, e.g. KG:= {(s,p,o)} union {(o,p_inverse,s)}
        if self.kg.add_reciprical and self.kg.eval_model:
            def adding_reciprocal_triples():
                """ Add reciprocal triples """
                # (1.1) Add reciprocal triples into training set
                self.kg.train_set.extend(self.kg.train_set.select([
                    pl.col("object").alias('subject'),
                    pl.col("relation").apply(lambda x: x + '_inverse'),
                    pl.col("subject").alias('object')
                ]))
                if self.kg.valid_set is not None:
                    # (1.2) Add reciprocal triples into valid_set set.
                    self.kg.valid_set.extend(self.kg.valid_set.select([
                        pl.col("object").alias('subject'),
                        pl.col("relation").apply(lambda x: x + '_inverse'),
                        pl.col("subject").alias('object')
                    ]))
                if self.kg.test_set is not None:
                    # (1.2) Add reciprocal triples into test set.
                    self.kg.test_set.extend(self.kg.test_set.select([
                        pl.col("object").alias('subject'),
                        pl.col("relation").apply(lambda x: x + '_inverse'),
                        pl.col("subject").alias('object')
                    ]))

            print('Adding Reciprocal Triples...')
            adding_reciprocal_triples()

        # (2) Type checking
        try:
            assert isinstance(self.kg.train_set, pl.DataFrame)
        except TypeError:
            raise TypeError(f"{type(self.kg.train_set)}")
        assert isinstance(self.kg.valid_set, pl.DataFrame) or self.kg.valid_set is None
        assert isinstance(self.kg.test_set, pl.DataFrame) or self.kg.test_set is None

        def concat_splits(train, val, test):
            x = [train]
            if val is not None:
                x.append(val)
            if test is not None:
                x.append(test)
            return pl.concat(x)

        print('Concat Splits...')
        df_str_kg = concat_splits(self.kg.train_set, self.kg.valid_set, self.kg.test_set)

        print('Entity Indexing...')
        self.kg.entity_to_idx = pl.concat((df_str_kg['subject'],
                                           df_str_kg['object'])).unique(maintain_order=True).rename('entity')
        print('Relation Indexing...')
        self.kg.relation_to_idx = df_str_kg['relation'].unique(maintain_order=True)
        print('Creating index for entities...')
        self.kg.entity_to_idx = {ent: idx for idx, ent in enumerate(self.kg.entity_to_idx.to_list())}
        print('Creating index for relations...')
        self.kg.relation_to_idx = {rel: idx for idx, rel in enumerate(self.kg.relation_to_idx.to_list())}
        self.kg.num_entities, self.kg.num_relations = len(self.kg.entity_to_idx), len(self.kg.relation_to_idx)

        print(f'Indexing Training Data {self.kg.train_set.shape}...')
        self.kg.train_set = self.kg.train_set.with_columns(
            pl.col("subject").map_dict(self.kg.entity_to_idx).alias("subject"),
            pl.col("relation").map_dict(self.kg.relation_to_idx).alias("relation"),
            pl.col("object").map_dict(self.kg.entity_to_idx).alias("object")).to_numpy()
        if self.kg.valid_set is not None:
            print(f'Indexing Val Data {self.kg.valid_set.shape}...')
            self.kg.valid_set = self.kg.valid_set.with_columns(
                pl.col("subject").map_dict(self.kg.entity_to_idx).alias("subject"),
                pl.col("relation").map_dict(self.kg.relation_to_idx).alias("relation"),
                pl.col("object").map_dict(self.kg.entity_to_idx).alias("object")).to_numpy()
        if self.kg.test_set is not None:
            print(f'Indexing Test Data {self.kg.test_set.shape}...')
            self.kg.test_set = self.kg.test_set.with_columns(
                pl.col("subject").map_dict(self.kg.entity_to_idx).alias("subject"),
                pl.col("relation").map_dict(self.kg.relation_to_idx).alias("relation"),
                pl.col("object").map_dict(self.kg.entity_to_idx).alias("object")).to_numpy()
        print(f'*** Preprocessing Train Data:{self.kg.train_set.shape} with Polars DONE ***')

    def sequential_vocabulary_construction(self) -> None:
        """
        (1) Read input data into memory
        (2) Remove triples with a condition
        (3) Serialize vocabularies in a pandas dataframe where
                    => the index is integer and
                    => a single column is string (e.g. URI)
        """
        try:
            assert isinstance(self.kg.train_set, pd.DataFrame)
        except AssertionError:
            raise AssertionError
            print(type(self.kg.train_set))
            print('HEREE')
            exit(1)
        assert isinstance(self.kg.valid_set, pd.DataFrame) or self.kg.valid_set is None
        assert isinstance(self.kg.test_set, pd.DataFrame) or self.kg.test_set is None

        # (4) Remove triples from (1).
        self.remove_triples_from_train_with_condition()
        # Concatenate dataframes.
        print('Concatenating data to obtain index...')
        x = [self.kg.train_set]
        if self.kg.valid_set is not None:
            x.append(self.kg.valid_set)
        if self.kg.test_set is not None:
            x.append(self.kg.test_set)
        df_str_kg = pd.concat(x, ignore_index=True)
        del x
        print('Creating a mapping from entities to integer indexes...')
        # (5) Create a bijection mapping from entities of (2) to integer indexes.
        # ravel('K') => Return a contiguous flattened array.
        # ‘K’ means to read the elements in the order they occur in memory,
        # except for reversing the data when strides are negative.
        ordered_list = pd.unique(df_str_kg[['subject', 'object']].values.ravel('K')).tolist()
        self.kg.entity_to_idx = {k: i for i, k in enumerate(ordered_list)}
        # 5. Create a bijection mapping  from relations to integer indexes.
        ordered_list = pd.unique(df_str_kg['relation'].values.ravel('K')).tolist()
        self.kg.relation_to_idx = {k: i for i, k in enumerate(ordered_list)}
        del ordered_list

    def remove_triples_from_train_with_condition(self):
        if None:
            # self.kg.min_freq_for_vocab is not
            assert isinstance(self.kg.min_freq_for_vocab, int)
            assert self.kg.min_freq_for_vocab > 0
            print(
                f'[5 / 14] Dropping triples having infrequent entities or relations (>{self.kg.min_freq_for_vocab})...',
                end=' ')
            num_triples = self.kg.train_set.size
            print('Total num triples:', num_triples, end=' ')
            # Compute entity frequency: index is URI, val is number of occurrences.
            entity_frequency = pd.concat([self.kg.train_set['subject'], self.kg.train_set['object']]).value_counts()
            relation_frequency = self.kg.train_set['relation'].value_counts()

            # low_frequency_entities index and values are the same URIs: dask.dataframe.core.DataFrame
            low_frequency_entities = entity_frequency[
                entity_frequency <= self.kg.min_freq_for_vocab].index.values
            low_frequency_relation = relation_frequency[
                relation_frequency <= self.kg.min_freq_for_vocab].index.values
            # If triple contains subject that is in low_freq, set False do not select
            self.kg.train_set = self.kg.train_set[~self.kg.train_set['subject'].isin(low_frequency_entities)]
            # If triple contains object that is in low_freq, set False do not select
            self.kg.train_set = self.kg.train_set[~self.kg.train_set['object'].isin(low_frequency_entities)]
            # If triple contains relation that is in low_freq, set False do not select
            self.kg.train_set = self.kg.train_set[~self.kg.train_set['relation'].isin(low_frequency_relation)]
            # print('\t after dropping:', df_str_kg.size.compute(scheduler=scheduler_flag))
            print('\t after dropping:', self.kg.train_set.size)  # .compute(scheduler=scheduler_flag))
            del low_frequency_entities

    def apply_reciprical_or_noise(self) -> None:
        """ (1) Add reciprocal triples (2) Add noisy triples """
        # (1) Add reciprocal triples, e.g. KG:= {(s,p,o)} union {(o,p_inverse,s)}
        if self.kg.add_reciprical and self.kg.eval_model:
            print('Adding reciprocal triples '
                  'to train, validation, and test sets, e.g. KG:= {(s,p,o)} union {(o,p_inverse,s)}')
            self.kg.train_set = create_recipriocal_triples(self.kg.train_set)
            if self.kg.valid_set is not None:
                self.kg.valid_set = create_recipriocal_triples(self.kg.valid_set)
            if self.kg.test_set is not None:
                self.kg.test_set = create_recipriocal_triples(self.kg.test_set)
