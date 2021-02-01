from django.shortcuts import render, redirect
from django.http import Http404
from death_user.models import Deathuser
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
                board = Board() 
                board.title = form.cleaned_data['title']
                board.contents = form.cleaned_data['contents']
                board.writer = deathuser
                board.save()

                return redirect('/board/list/')
        else:
            form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    boards = Board.objects.all().order_by('-id') # 가장 최신 것을 먼저가져오겠다.
    return render(request, 'board_list.html', {'boards': boards})