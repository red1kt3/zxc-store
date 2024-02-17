from rest_framework import permissions, viewsets

from apps.api.blog.serializers import ArticleSerializer
from apps.blog.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        try:
            if self.request.query_params.get('category'):
                queryset = queryset.filter(category=self.request.query_params['category'])
            if self.request.query_params.get('user'):
                queryset = queryset.filter(user_id=self.request.query_params['user'])
        except AttributeError:
            pass
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




