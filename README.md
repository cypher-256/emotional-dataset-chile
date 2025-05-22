---
annotations_creators:
- manual
language:
- es
license: mit
multilinguality: monolingual
pretty_name: Emotional Dataset Chile
task_categories:
- text-classification
task_ids:
- sentiment-classification
tags:
- valence
- arousal
- spanish
- chile
---

# Emotional Dataset Chile

Este repositorio contiene un conjunto de datos emocional en español chileno, curado para tareas de regresión continua en valencia y arousal. Fue desarrollado como parte de un proyecto experimental enfocado en el entrenamiento de modelos multitarea con BERT y LoRA.

## 📘 Descripción

El dataset está formado por ejemplos de texto en español chileno informal, etiquetados manual o semi-automáticamente con valores de:

- **Valencia**: grado de positividad/negatividad emocional (-1.0 a 1.0)
- **Arousal**: grado de activación o intensidad emocional (-1.0 a 1.0)

### Archivos disponibles

- `valencia_dataset.jsonl`: muestras con etiqueta de valencia.
- `arousal_dataset.jsonl`: muestras con etiqueta de arousal.

Cada archivo está en formato JSON Lines (`.jsonl`), donde cada línea contiene:

```json
{
  "texto": "Hoy terminé mi proyecto, estoy eufórico.",
  "arousal": 0.91
}
```

---

(English version)

# Emotional Dataset Chile

This repository contains an emotional dataset in Chilean Spanish, curated for continuous regression tasks on **valence** and **arousal**. It was developed as part of an experimental project focused on multitask training with BERT and LoRA.

## 📘 Description

The dataset consists of informal Chilean Spanish text samples, manually or semi-automatically labeled with:

- **Valence**: degree of emotional positivity or negativity (ranging from -1.0 to 1.0)
- **Arousal**: degree of emotional intensity or activation (ranging from -1.0 to 1.0)

### Available files

- `valencia_dataset.jsonl`: samples labeled with valence scores.
- `arousal_dataset.jsonl`: samples labeled with arousal scores.

Each file follows the JSON Lines format (`.jsonl`), with one JSON object per line:

```json
{
  "texto": "Hoy terminé mi proyecto, estoy eufórico.",
  "arousal": 0.91
}
```

---

## 🧪 Ejemplo de uso HF

```python
from datasets import load_dataset
import pandas as pd

# Cargar la configuración de valencia
valencia_ds = load_dataset(
    "cypher-256/emotional-dataset-chile",
    "valencia",
    trust_remote_code=True
)
valencia_df = pd.DataFrame(valencia_ds["train"])

# Cargar la configuración de arousal
arousal_ds = load_dataset(
    "cypher-256/emotional-dataset-chile",
    "arousal",
    trust_remote_code=True
)
arousal_df = pd.DataFrame(arousal_ds["train"])

# Mostrar los primeros registros
print("Ejemplos - VALENCIA:")
print(valencia_df.head())

print("\nEjemplos - AROUSAL:")
print(arousal_df.head())
```

## 🏠 Ejemplo de uso local

1. Clona el repositorio:
    ```bash
    git clone https://github.com/cypher-256/emotional-dataset-chile
    ```

2. Usa el dataset con su ruta local:
    ```python
    from datasets import load_dataset
    import pandas as pd

    # Carga local como si fuera JSON Lines
    valencia_ds = load_dataset(
        "json",
        data_files="emotional-dataset-chile/valencia_dataset.jsonl",
        split="train"
    )
    arousal_ds = load_dataset(
        "json",
        data_files="emotional-dataset-chile/arousal_dataset.jsonl",
        split="train"
    )

    # Convierte a DataFrame
    valencia_df = pd.DataFrame(valencia_ds)
    arousal_df  = pd.DataFrame(arousal_ds)

    print("Ejemplos – VALENCIA:")
    print(valencia_df.head())

    print("\nEjemplos – AROUSAL:")
    print(arousal_df.head())
    ```


---

---

## 💸 Donaciones

Si este dataset te ha sido útil y deseas apoyar su desarrollo, puedes contribuir con una donación en Bitcoin o Monero. Estas contribuciones ayudan a mantener y expandir recursos abiertos para el procesamiento del lenguaje en español chileno.

### Bitcoin (BTC – On-chain)

**Dirección:**  
`bc1p2t0gfxe3c0yw3rm3mdpgkrqwrpphgklhdt55lus3lmp4e86ljhnq4qkmp6`

> Puedes usar cualquier billetera compatible con direcciones Taproot (P2TR), como Muun, Sparrow o BlueWallet.

<img src="assets/donacion_btc.png" alt="BTC QR" width="200"/>

---

### Monero (XMR – Anónimo)

**Dirección:**  
`44dS68RZrCY2cnoEWZYhtJJ3DXY52x75D2kCTLqffhpTWCFJUcty89W2VVUKCqE4J4WH8dnUJHCT1XQsXFkEKNyvQzqx8ar`

> Puedes usar billeteras como Feather Wallet, Monerujo o Cake Wallet.

<img src="assets/donacion_xmr.png" alt="XMR QR" width="200"/>

---

Gracias por apoyar el software libre y la investigación abierta.

