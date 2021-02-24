from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from death_user.models import Deathuser
from tag.models import Tag
from .models import Board
from .forms import BoardForm

# Create your views here.

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    user_id = request.session.get('user') # 세션으로부터 가져옴
    if not user_id:
        return redirect('/death_user/login')
    else:
        if request.method == 'POST':
            form = BoardForm(request.POST)
            if form.is_valid():
                deathuser = Deathuser.objects.get(pk=user_id)

                tags = form.cleaned_data['tags'].split(',')

                board = Board() 
                board.title = form.cleaned_data['title']
                board.contents = form.cleaned_data['contents']
                board.writer = deathuser
                board.save()
                for tag in tags:
                    if not tag:
                        continue
                    
                    _tag, created = Tag.objects.get_or_create(name=tag)
                    board.tags.add(_tag)
                
                return redirect('/board/list/')
        else:
            form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # 가장 최신 것을 먼저가져오겠다.
    page = request.GET.get('p', 1) 
    paginator = Paginator(all_boards, 5)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})