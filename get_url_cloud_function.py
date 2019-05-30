from swfastwork import cloud_function

def get_url_cloud_function(request, context):

   request, context = cloud_function.start(request, context)

   print(request)

   url = 'http://google.com/'

   return cloud_function.end({
       'url' : url
   })

