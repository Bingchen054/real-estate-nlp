import re
import unicodedata
from collections import Counter
import nltk

class TextCleaner:

    def __init__(self):
        self.abbrev_map = {
            'br': 'bedroom',
            'bd': 'bedroom',
            'ba': 'bathroom',
            'bth': 'bathroom',
            'sqft': 'square feet',
            'sf': 'square feet',
            'w/': 'with',
            'w/o': 'without',
            'mbr': 'master bedroom',
            'lr': 'living room',
            'dr': 'dining room',
            'kit': 'kitchen',
            'hw': 'hardwood',
            'ac': 'air conditioning',
            'hvac': 'heating ventilation air conditioning',
            'hoa': 'home owners association',
            'fp': 'fireplace',
            'pkg': 'parking',
            'apt': 'apartment',
            'condo': 'condominium',
            'remod': 'remodeled',
            'reno': 'renovated',
            'lg': 'large',
            'sm': 'small',
            'yr': 'year',
            'yrs': 'years',
            'min': 'minutes',
            'sec': 'seconds',
            'approx': 'approximately',
            'est': 'estimated',
            'incl': 'included',
            'excl': 'excluded',
            'flr': 'floor',
            'bsmt': 'basement'
        }

    # ======================
    # MAIN PIPELINE
    # ======================

    def clean_text(self, text):
        if not isinstance(text, str):
            return ""

        text = self.normalize_unicode(text)
        text = self.remove_html(text)
        text = self.normalize_prices(text)
        text = self.normalize_measurements(text)
        text = self.expand_abbreviations(text)
        text = self.remove_extra_whitespace(text)

        return text.strip()

    # ======================
    # NORMALIZATION METHODS
    # ======================

    def normalize_unicode(self, text):
        return unicodedata.normalize("NFKD", text)

    def remove_html(self, text):
        return re.sub(r'<.*?>', '', text)

    def normalize_prices(self, text):
        # 450k → 450000
        text = re.sub(
            r'(\d+)\s*k\b',
            lambda m: str(int(m.group(1)) * 1000),
            text,
            flags=re.I
        )

        # 1.2m → 1200000
        text = re.sub(
            r'(\d+\.?\d*)\s*m\b',
            lambda m: str(int(float(m.group(1)) * 1000000)),
            text,
            flags=re.I
        )

        return text

    def normalize_measurements(self, text):
        # 2,000 sqft → 2000 square feet
        text = re.sub(r'(\d{1,3}(?:,\d{3})+)', lambda m: m.group(1).replace(',', ''), text)

        text = re.sub(
            r'(\d+)\s*(sqft|sf)\b',
            r'\1 square feet',
            text,
            flags=re.I
        )

        return text

    def expand_abbreviations(self, text):
        tokens = text.split()
        expanded = []

        for token in tokens:
            clean_token = token.lower()
            if clean_token in self.abbrev_map:
                expanded.append(self.abbrev_map[clean_token])
            else:
                expanded.append(token)

        return " ".join(expanded)

    def remove_extra_whitespace(self, text):
        return re.sub(r'\s+', ' ', text)

    # ======================
    # PROFILING
    # ======================

    def profile_column(self, df, column_name):

        col = df[column_name].dropna()

        return {
            'null_rate': df[column_name].isnull().mean(),
            'avg_length': col.str.len().mean(),
            'price_mentions': col.str.contains(r'\$\d').sum(),
            'has_html': col.str.contains(r'<').sum(),
            'common_terms': self._extract_top_ngrams(col),
            'common_abbreviations': self._detect_abbreviations(col)
        }

    def _extract_top_ngrams(self, series, n=2, top_k=20):
        all_text = " ".join(series.str.lower())
        tokens = nltk.word_tokenize(all_text)

        ngrams = zip(*[tokens[i:] for i in range(n)])
        freq = Counter(ngrams)

        return freq.most_common(top_k)

    def _detect_abbreviations(self, series):
        abbrev_counts = Counter()

        for text in series:
            tokens = text.lower().split()
            for token in tokens:
                if token in self.abbrev_map:
                    abbrev_counts[token] += 1

        return abbrev_counts.most_common(20)