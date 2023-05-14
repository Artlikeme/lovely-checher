from rest_framework import permissions, filters
from rest_framework.generics import ListCreateAPIView, \
    ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from item.models import Item, ItemThroughIp, Comment, Favorite
from item.serializers import ItemGetSerializer, \
    ItemPostSerializer, TopThreeItemSerializer, SingleItemSerializer, \
    LastViewsItemSerializer, CommentPostPostSerializer, CommentGetPostSerializer,\
    FavoritePOSTSerializer, FavoriteGETSerializer
from main.services.get_top_three import get_top_three_items
from main.services.get_user_city import get_user_city
from main.services.views_add import add_view


class ItemListPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100


class ItemSearchView(ListCreateAPIView):
    serializer_class = ItemGetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = ItemListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        return Item.objects.filter(city__name=get_user_city(self.request))


class ItemListCreateView(ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = ItemListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__name']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemPostSerializer
        else:
            return ItemGetSerializer

    def get_queryset(self):
        return Item.objects.filter(city__name=get_user_city(self.request))

    def post(self, request, *args, **kwargs):
        response = super().post(request, args, kwargs)
        return response


class SingleItemView(RetrieveAPIView):
    queryset = Item.objects.filter(active=True)
    serializer_class = SingleItemSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, args, kwargs)
        # добавление шз адреса в просмотры
        add_view(request, self.queryset, **kwargs)

        return response


class TopThreeItems(ListAPIView):
    serializer_class = TopThreeItemSerializer

    def get_queryset(self):
        return get_top_three_items(self.request)


class LastThreeItems(ListAPIView):
    serializer_class = LastViewsItemSerializer

    def get_queryset(self):
        return ItemThroughIp.objects \
                   .select_related('item', 'item__category') \
                   .filter(ip__ip=get_user_city(self.request, get_ip=True),
                           item__active=True) \
                   .only('item__title',
                         'item__image',
                         'item__rating',
                         'item__category'
                         ) \
                   .order_by('-date')[0:3]


class CommentsView(ListCreateAPIView):
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentPostPostSerializer
        else:
            return CommentGetPostSerializer


class FavoriteView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FavoritePOSTSerializer
        else:
            return FavoriteGETSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
