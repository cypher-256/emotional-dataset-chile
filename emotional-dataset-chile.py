import json
import datasets

_CITATION = """\
@misc{quintero2024emotionaldatasetchile,
  author       = {cypher-256},
  title        = {Emotional Dataset Chile},
  year         = 2025,
  url          = {https://huggingface.co/datasets/cypher-256/emotional-dataset-chile}
}
"""

_DESCRIPTION = """\
Este dataset contiene ejemplos en español chileno etiquetados con valencia o arousal emocional \
en formato de regresión continua (-1.0 a 1.0). Incluye dos configuraciones independientes: 'valencia' y 'arousal'.
"""

_HOMEPAGE = "https://huggingface.co/datasets/cypher-256/emotional-dataset-chile"

_LICENSE = "MIT"

_DATA_FILES = {
    "valencia": "valencia_dataset.jsonl",
    "arousal": "arousal_dataset.jsonl",
}

class EmotionalDatasetChileConfig(datasets.BuilderConfig):
    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)

class EmotionalDatasetChile(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        EmotionalDatasetChileConfig(
            name="valencia",
            version=datasets.Version("1.0.0"),
            description="Text samples labeled with emotional valence",
        ),
        EmotionalDatasetChileConfig(
            name="arousal",
            version=datasets.Version("1.0.0"),
            description="Text samples labeled with emotional arousal",
        ),
    ]

    def _info(self):
        features = datasets.Features(
            {
                "texto": datasets.Value("string"),
                self.config.name: datasets.Value("float32"),
            }
        )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        data_file = _DATA_FILES[self.config.name]
        data_path = dl_manager.download_and_extract(data_file)
        return [datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_path})]

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            for idx, line in enumerate(f):
                data = json.loads(line)
                yield idx, data
