Modelo clasificatorio de calidad de Vino, usando múltiples modelos donde se escogió un RandomForest como el mejor modelo. A partir de este modelo, se creó un app en Flask para la clasificación de ejemplos de vinos.

Por: Fabián Manrique

############################Comandos GCP#################################

############################ Compilacion de contenedor###########

mkdir gcprunbase
cd gcprunbase

PROJECT_ID=$(gcloud config get-value project)
echo $PROJECT_ID
DOCKER_IMG="gcr.io/$PROJECT_ID/basecloudrun"
echo $DOCKER_IMG
gcloud builds submit --tag $DOCKER_IMG .

gcloud container images list

#################################Link app#################################
Link Modelo Clasificador
https://vino-classifier-txqzymuqva-uc.a.run.app/predict
##############################################################################

################################# Validacion #################################
docker pull $DOCKER_IMG
docker run -p 8080:8080 $DOCKER_IMG
##############################################################################



################################# Comandos Flask #################################
python3 -m venv env
.\env\bin\activte
pip install -r requirements.txt
python3 app.py
##############################################################################
