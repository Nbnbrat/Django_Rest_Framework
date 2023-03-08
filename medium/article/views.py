from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Author
from .serializers import ArticleSerializer

# Create your views here.


class ArticleView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = ArticleSerializer(articles,many=True)
        return Response({"articles": serializer.data})

    def post(self,request):
        article = request.data.get('articles')

        # create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({article_saved.title},{article_saved.body})


    # def put(self,request,pk):
    #     saved_article = get_object_or_404(Article.objects.all(),pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article,data=data,partial=True) # bcz we want to update only some fields not  a whole article so partial is true
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success":f"Article {article_saved.title} updated successfully."})
    #
    # def delete(self,request,pk):
    #     # get object with this pk
    #     article = get_object_or_404(Article.objects.all(),pk=pk)
    #     article.delete()
    #     return Response({"message":f"Article with id {pk} has been deleted."},status=204)

