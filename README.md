# Simple ML Training Project
This project trains a RandomForest model on tabular data.# pontia-mlops-tutorial
# pontia-mlops-tutorial
# prueba-real


# Build.yml

                GitHub Actions
                      │
                      ▼
              Ubuntu Runner
                      │
                      ▼
          Descargar dataset
                      │
                      ▼
           Preprocesar datos
                      │
                      ▼
            Entrenar modelo
                      │
                      ▼
        model.pkl scaler.pkl encoders.pkl
                      │
          ┌───────────┴────────────┐
          │                        │
          ▼                        ▼
GitHub Artifact             Azure MLflow
(model.pkl)                 │
                             ├── Nueva Run
                             ├── Métricas
                             ├── Modelo
                             ├── Artefactos
                             └── Registro del modelo



| Acción                             | integration.yml | build.yml                    | deploy.yml                  |
|--------                            |-----------------|-----------                   |------------                 |
| `git push origin deploy`           | ❌              | ❌ (si escucha solo `main`)  | ❌ (si escucha solo `main`) |
| Crear Pull Request `deploy → main` | ✅              | ❌                          | ❌                          |
| `git push origin deploy` con PR abierto | ✅         | ❌                          | ❌                          |
| Merge del PR a `main`              | ❌ (el PR ya terminó) | ✅                    | ✅                          |
| `git push origin main`             | ❌              | ✅                          | ✅                          |


# Flujo de PR para los tres workflows en accion (deploy es una rama de ejemplo)

             Desarrollo
                 |
                 v
              deploy
                 |
          git push origin deploy
                 |
                 v
          Pull Request
                 |
                 v
          integration.yml
                 |
                 v
          Merge en GitHub
                 |
                 v
               main
                 |
        ┌────────┴────────┐
        v                 v
    build.yml        deploy.yml
        |                 |
   Entrenar ML      Azure Container App