class Normalizer:
    """
    A class to handle the normalization of characters and words for sentences.
    It uses predefined groups of characters and words to create normalization maps 
    and apply them to sentences for consistent normalization.

    Attributes:
        normalization_map (dict): A dictionary mapping characters to their canonical form.
        normalization_word (dict): A dictionary mapping words to their canonical form.
    """

    def __init__(self, homo_groups, norm_groups):
        """
        Initializes the Normalizer with the given character and word groups for normalization.

        Args:
            homo_groups (list): A list of groups of similar characters for normalization.
            norm_groups (list): A list of groups of similar words for normalization.
        """
        self.normalization_map = self._generate_normalization_map(homo_groups)
        self.normalization_word = self._generate_word_normalization_map(norm_groups)

    def _generate_normalization_map(self, homo_groups):
        """
        Generates a normalization map for characters based on the given groups of similar characters.

        Args:
            homo_groups (list): A list of groups of similar characters.

        Returns:
            dict: A dictionary mapping each character to its canonical form.
        """
        normalization_map = {}
        for group in homo_groups:
            canonical_char = group[0]  # Use the first element as the canonical character
            for char in group:
                normalization_map[char] = canonical_char
        return normalization_map

    def _generate_word_normalization_map(self, norm_groups):
        """
        Generates a normalization map for words based on the given groups of similar words.

        Args:
            norm_groups (list): A list of groups of similar words.

        Returns:
            dict: A dictionary mapping each word to its canonical form.
        """
        normalization_word = {}
        for group in norm_groups:
            canonical_word = group[0]  # Use the first word as the canonical word
            for word in group:
                normalization_word[word] = canonical_word
        return normalization_word

    def normalize_chars_for_sentence(self, sentence):
        """
        Normalizes an entire sentence at the character level using the character normalization map.

        Args:
            sentence (str): The sentence to normalize.

        Returns:
            str: The normalized sentence at the character level.
        """
        return ''.join([self.normalization_map.get(char, char) for char in sentence])

    def normalize_words_for_sentence(self, sentence):
        """
        Normalizes an entire sentence at the word level using the word normalization map.

        Args:
            sentence (str): The sentence to normalize.

        Returns:
            str: The normalized sentence at the word level.
        """
        return ' '.join([self.normalization_word.get(word, word) for word in sentence.split()])

    def normalize_sentence(self, sentence, level='char'):
        """
        Normalizes a sentence at the specified level (character or word).

        Args:
            sentence (str): The sentence to normalize.
            level (str): The normalization level ('char' for character-level, 'word' for word-level).

        Returns:
            str: The normalized sentence.
        """
        if level == 'char':
            return self.normalize_chars_for_sentence(sentence)
        elif level == 'word':
            return self.normalize_words_for_sentence(sentence)
        else:
            raise ValueError("Normalization level must be 'char' or 'word'.")

    def normalize_sentences(self, sentences, level='char'):
        """
        Normalizes a list or a dictionary of sentences at the specified level (character or word).

        Args:
            sentences (list or dict): A list of sentences or a dictionary with sentence keys and values to normalize.
            level (str): The normalization level ('char' for character-level, 'word' for word-level).

        Returns:
            list or dict: A list or a dictionary of normalized sentences.
        """
        if isinstance(sentences, list):
            # Normalize a list of sentences
            if level == 'char':
                return [self.normalize_chars_for_sentence(sentence) for sentence in sentences]
            elif level == 'word':
                return [self.normalize_words_for_sentence(sentence) for sentence in sentences]
            else:
                raise ValueError("Normalization level must be 'char' or 'word'.")
        elif isinstance(sentences, dict):
            # Normalize each sentence in the dictionary (each key corresponds to a sentence)
            if level == 'char':
                return {key: self.normalize_chars_for_sentence(value) for key, value in sentences.items()}
            elif level == 'word':
                return {key: self.normalize_words_for_sentence(value) for key, value in sentences.items()}
            else:
                raise ValueError("Normalization level must be 'char' or 'word'.")
        else:
            raise TypeError("Input must be a list or a dictionary.")