document.addEventListener('DOMContentLoaded', function(){
    const toogleComm= document.getElementById('toggleComments');
    const commentSect= document.getElementById('commentSection');
    toogleComm.addEventListener('click',function(){
        if(commentSect.classList.contains('comments_hidden')){
            commentSect.classList.remove('comments_hidden');
            toogleComm.innerText = 'Hide Comments';
        }else{
            commentSect.classList.add('comments_hidden');
            toogleComm.innerText = 'Show Comments';
        }
    })
})