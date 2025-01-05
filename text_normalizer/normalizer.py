# normalizer.py

from .char_norm import char_groups
from .word_norm import word_groups

class Normalizer:
    def __init__(self):
        # Generate normalization maps for characters and words when initializing the class
        self.normalization_map = self._generate_normalization_map(char_groups)
        self.normalization_word = self._generate_word_normalization_map(word_groups)
    
    def _generate_normalization_map(self, homo_groups):
        """
        Generates a normalization map for characters, where similar characters
        are normalized to the first character in each group.
        """
        normalization_map = {}
        for group in homo_groups:
            canonical_char = group[0]  # Use the first character as the canonical character
            for char in group:
                normalization_map[char] = canonical_char
        return normalization_map

    def _generate_word_normalization_map(self, norm_groups):
        """
        Generates a normalization map for words, where similar words are normalized
        to the first word in each group.
        """
        normalization_word = {}
        for group in norm_groups:
            canonical_word = group[0]  # Use the first word as the canonical word
            for word in group:
                normalization_word[word] = canonical_word
        return normalization_word

    def normalize_sentence(self, sentence, level='char'):
        """
        Normalizes a sentence either at the character level or word level.
        """
        if level == 'char':
            return self.normalize_chars_for_sentence(sentence)
        elif level == 'word':
            return self.normalize_words_for_sentence(sentence)
        else:
            raise ValueError("Normalization level must be 'char' or 'word'.")

    def normalize_chars_for_sentence(self, sentence):
        """
        Normalize the characters in the sentence based on the character normalization map.
        """
        return ''.join([self.normalization_map.get(char, char) for char in sentence])

    def normalize_words_for_sentence(self, sentence):
        """
        Normalize the words in the sentence based on the word normalization map.
        """
        return ' '.join([self.normalization_word.get(word, word) for word in sentence.split()])
