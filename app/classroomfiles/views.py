from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import ClassRoomFiles
from .serializers import ClassRoomFilesSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
import re
import urllib.request
from nltk.util import ngrams, pad_sequence, everygrams
from nltk.tokenize import word_tokenize
from nltk.lm import MLE, WittenBellInterpolated
import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter
class ClassRoomFilesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=ClassRoomFiles.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ClassRoomFilesSerializer

    def create(self,request):
        res = request.data
        s = ClassRoomFilesSerializer(data=res)
        s.is_valid(raise_exception=True)
        s.save()
        # print(open(res.get('files').path).read())
        print(s.data)
        recognition(s.data.get('files'))
        ClassRoomFiles.objects.filter(id=s.data['id']).update(results=recognition(s.data.get('files')))
        return Response(data = {})
        


class GetFileByProfID(generics.GenericAPIView):
    def get(self,request,format=None,folder_id=None):
        items = ClassRoomFiles.objects.filter(folder_id=folder_id)
        items = ClassRoomFilesSerializer(items,many=True)
        return Response(data = items.data)




def recognition(url):
    link = url
    f = urllib.request.urlopen(link)           
    myfile = f.read()

    # with open(train_data_file) as f:
    #     open(train_data_file)
    #     train_text = f.read().lower()
    #     print(train_text)
    train_text = re.sub(r"\[.*\]|\{.*\}", "", myfile.decode("utf-8"))
    train_text = re.sub(r'[^\w\s]', "", myfile.decode("utf-8"))
    n = 4
    training_data = list(pad_sequence(word_tokenize(train_text), n, 
                                    pad_left=True, 
                                    left_pad_symbol="<s>"))
    ngrams = list(everygrams(training_data, max_len=n))
    print("Number of ngrams:", len(ngrams))
    model = WittenBellInterpolated(n)
    model.fit([ngrams], vocabulary_text=training_data)
    test_data_file = "test.docx"
    with open(test_data_file) as f:
        test_text = f.read().lower()
    test_text = re.sub(r'[^\w\s]', "", test_text)
    testing_data = list(pad_sequence(word_tokenize(test_text), n, 
                                    pad_left=True,
                                    left_pad_symbol="<s>"))
    scores = []
    for i, item in enumerate(testing_data[n-1:]):
        s = model.score(item, testing_data[i:i+n-1])
        scores.append(s)
    scores_np = np.array(scores)
    print(f"score {max(scores_np)}")
    return max(scores_np)