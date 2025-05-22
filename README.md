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