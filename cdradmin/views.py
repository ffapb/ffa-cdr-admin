from django.http import HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from .models import SuperidToLoanLiability
from .models import EntityToPartnerType
from django.http import JsonResponse
from django.core import serializers
import json

#from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict



class IndexView( generic.ListView):
    template_name = 'cdradmin/index.html'
    
    model= SuperidToLoanLiability
    
    def get_queryset(self):
        """Return the superid by order alphabetic."""
        return SuperidToLoanLiability.objects.order_by('superid')
   
    def get(self, *args, **kwargs):
    
        asjson = self.request.GET.get('asjson', "false")
        asjson=asjson.lower()=="true"
          
        if not asjson:
            return super(IndexView, self).get(*args, **kwargs)
        
   
        
             
        #https://stackoverflow.com/questions/41116841/object-is-not-json-serializable-django
        #to get the id of foreignkey
        #data = SuperidToLoanLiability.objects.all().values('superid', 'loan', 'liability')
        #data = SuperidToLoanLiability.objects.all()[0]
        json_obj = [
          {
            "superid": x.superid.superid,
            "loan_type": x.loan_type.short_description,
            "liability_type": x.liability_type.short_description,
            "ledger": x.ledger.ledger
          } for x in SuperidToLoanLiability.objects.all()
        ]
        return JsonResponse(json_obj ,safe=False)



class EntityListView(ListView):

    template_name='cdradmin/entity_partnertype.html'
    #context_object_name = 'entity_partner_type'
    model = EntityToPartnerType
    

      
    def get_queryset(self):
        """Return the entity by order asc."""
        return EntityToPartnerType.objects.order_by('entity')
       
    def get(self, *args, **kwargs):   
         asjson = self.request.GET.get('asjson', "false")
         asjson=asjson.lower()=="true"

         if not asjson:
            return super().get(*args, **kwargs)


         json_obj = [
           {
            "entity": y.entity
         #   "partner_type": y.partner_type
            
          
            } for y in EntityToPartnerType.objects.all()
         ]
         return JsonResponse(json_obj,safe=False)
#         return HttpResponse(json.simplejson.dumps(json_obj), mimetype="application/json")
   
   #      return HttpResponse(data, content_type="application/json") 

         #context['entity'] = ([x.entity for x in context['object_list']]);
         #context['partner_type'] = ([x.partner_type for x in context['object_list']]);
        
         
                              

