        
# To load shape file into the database
# Step 1 Run the ogrinstect
# python manage.py ogrinspect [options] <data_source> <model_name> [options]
# in this case
# eg. python manage.py ogrinspect shp/Local.shp  Local  --srid=4326 --mapping --multi
# run manage.py shell
##this will generate following code in terminal
# class Local(models.Model):
#     province = models.BigIntegerField()
#     pr_name = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)
#     local = models.CharField(max_length=50)
#     type = models.CharField(max_length=50)
#     geom = models.MultiPolygonField(srid=4326)


# # Auto-generated `LayerMapping` dictionary for Local model
# local_mapping = {
#     'province': 'PROVINCE',
#     'pr_name': 'PR_NAME',
#     'district': 'DISTRICT',
#     'local': 'LOCAL',
#     'type': 'TYPE',
#     'geom': 'MULTIPOLYGON',
# }

#copy model into the model.py -and then migrate
#now database table is set up according to the shp provide earlier in ogrinspect
#to load data in database from shp follow step 2

#Step 2
# >>> from django.contrib.gis.utils import LayerMapping
# >>> from geoapp.models import TestGeo

# >>>local_mapping = {
#     'province': 'PROVINCE',
#     'pr_name': 'PR_NAME',
#     'district': 'DISTRICT',
#     'local': 'LOCAL',
#     'type': 'TYPE',
#     'geom': 'MULTIPOLYGON',
# }

# >>> lm = LayerMapping(Local, 'Local.shp', local_mapping)
# >>> lm.save(verbose=True)     
#this will load 

#Routes to integrate in react JS 
#For Bagmati Municipality
# http://127.0.0.1:8000/api/search/custom?municipality__local=Bagmati
# http://127.0.0.1:8000/api/search/custom?municipality__local=Mahankal
# http://127.0.0.1:8000/api/search/custom?municipality__local=Lalitpur
# http://127.0.0.1:8000/api/search/custom?municipality__local=Konjyosom
#and so on for all the municpiplaity