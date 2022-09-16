const heartIcn = '<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M12 21.593c-5.63-5.539-11-10.297-11-14.402 0-3.791 3.068-5.191 5.281-5.191 1.312 0 4.151.501 5.719 4.457 1.59-3.968 4.464-4.447 5.726-4.447 2.54 0 5.274 1.621 5.274 5.181 0 4.069-5.136 8.625-11 14.402m5.726-20.583c-2.203 0-4.446 1.042-5.726 3.238-1.285-2.206-3.522-3.248-5.719-3.248-3.183 0-6.281 2.187-6.281 6.191 0 4.661 5.571 9.429 12 15.809 6.43-6.38 12-11.148 12-15.809 0-4.011-3.095-6.181-6.274-6.181"/></svg>';
const heartIcnLiked = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 4.248c-3.148-5.402-12-3.825-12 2.944 0 4.661 5.571 9.427 12 15.808 6.43-6.381 12-11.147 12-15.808 0-6.792-8.875-8.306-12-2.944z"/></svg>';
const HEART = '<ion-icon name="heart-outline"></ion-icon>';
const HEARTLIKED = '<ion-icon name="heart"></ion-icon>';
export function create_post() {

    // get the text of post
    let body = document.querySelector('#id_body');

    // make post request
    fetch('makePost', {
        method: 'POST',
        body: JSON.stringify({
            body: body.value,
        })
    })

    // reset the text input
    body.value = '';
    pageInd = 1;
    window.history.pushState({
        pageInd: pageInd
    }, '', `?page=${pageInd}`);
    loadPosts(pageInd);
}

export function loadPosts(page, filter = 'all') {
    let path = '';
    if (filter == 'all') {
        path = 'getPosts';
    } else if (filter == 'self') {
        const url = new URL(window.location.href)
        const username = url.pathname.replace('/', '');
        path = `getUserPosts/${username}`;
    } else if (filter == 'following') {
        path = 'getFollowing';
    }
    fetch(path + '?' + new URLSearchParams({
            page: page,
        }), {
            method: 'GET',
        })
        .then(result => result.json())
        .then(response => {

            const container = document.querySelector('#posts');
            response['posts'].forEach(element => {
                // div for post
                let div = document.createElement('div');
                div.className = 'Post';
                div.id = element['id']

                // username
                let username = document.createElement('a');
                username.innerHTML = element['username'];
                username.style.fontSize = '30px';
                username.href = element['username'];
                div.appendChild(username);


                // edit
                if (element['username'] == USERNAME) {
                    let edit = document.createElement('a');
                    edit.innerHTML = 'Edit';
                    edit.href = '';
                    edit.className = 'editBtn';
                    edit.dataset.id = element['id']
                    edit.onclick = () => {
                        editPost(element['id'])
                        return false;
                    }
                    edit.style.margin = '5px';
                    div.appendChild(edit);
                }


                // body
                let body = document.createElement('p');
                body.innerHTML = element['body'];
                body.id = `${element['id']}_body`
                div.appendChild(body);


                // timestamp
                let timestamp = document.createElement('p');
                timestamp.innerHTML = element['timestamp'];
                timestamp.id = `${element['id']}_timestamp`
                div.appendChild(timestamp);


                // likes 
                let likes = document.createElement('a');
                likes.href = ''


                // add onclick fucntion and icon
                if (element['isLiked'])
                {
                    likes.innerHTML = HEARTLIKED + ` ${element['likes']}`;

                    likes.onclick = () => {
                        dislikePost(element['id'])
                        return false;
                    }
                }
                else {
                    likes.innerHTML = HEART + ` ${element['likes']}`;
                    
                    likes.onclick = () => {
                        likePost(element['id'])
                        return false;
                    }
                }


                likes.style.textDecoration = 'none';
                likes.id = `${element['id']}_likes`
                likes.dataset.likes = element['likes'];
                div.appendChild(likes);

                // append to posts div
                container.appendChild(div);
            });
            // make both links enabled
            let link = document.querySelector('#prev_page').parentElement;
            link.className = link.className.replace('disabled', '');

            link = document.querySelector('#next_page').parentElement;
            link.className = link.className.replace('disabled', '');

            // if last or first page disabled next or prev link respectively
            if (page == 1) {
                let link = document.querySelector('#prev_page').parentElement;
                link.className = link.className + ' disabled';
                // console.log('disabled prev');
            }
            if (page == response['lastPage']) {
                let link = document.querySelector('#next_page').parentElement;
                link.className = link.className + ' disabled';
                // console.log('disabled next');
            }
        })
}

export function clearPosts() {
    const container = document.querySelector('#posts');
    let child = container.lastChild;
    while (child) {
        container.removeChild(child);
        child = container.lastChild;
    }
}

export function editPost(id) {
    // get id of elements
    const timestampId = `${id}_timestamp`;
    const bodyId = `${id}_body`


    // get that elements
    const timestamp = document.getElementById(timestampId);
    const body = document.getElementById(bodyId);

    // get parent div
    const parentDiv = body.parentNode;
    // save body of element
    let bodyInnerHTML = body.innerHTML;


    // create input
    let textArea = document.createElement('textarea');
    textArea.innerHTML = bodyInnerHTML;
    textArea.id = `${bodyId}`;
    textArea.className = 'NewPostBody';

    // insert new element and delete previous one
    parentDiv.insertBefore(textArea, body);
    body.remove();

    // change edit btn to save
    let editBtn = parentDiv.querySelector('.editBtn');
    editBtn.innerHTML = 'Save'
    editBtn.onclick = () => {
        savePost(id);
        return false;
    }

}

export function savePost(id) {
    // get inner html
    const bodyId = `${id}_body`;
    let bodyOld = document.getElementById(bodyId);
    const bodyValue = bodyOld.value;

    // create p tag and make post request
    let bodyNew = document.createElement('p')
    bodyNew.innerHTML = bodyValue;
    bodyNew.id = bodyId;

    // get parent div to delete and insert new element
    let parentDiv = bodyOld.parentNode;
    parentDiv.insertBefore(bodyNew, bodyOld);
    bodyOld.remove();

    // change button
    let editBtn = parentDiv.querySelector('.editBtn');
    editBtn.innerHTML = 'Edit';
    editBtn.onclick = () => {
        editPost(id);
        return false;
    }


    // make post request
    fetch(`${id}/edit`, {
            method: "POST",
            body: JSON.stringify({
                body: bodyValue
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })
}

export function likePost(id) {
    const path = `${id}/like`
    fetch(path, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })
    // change quantity of likes
    let likeBtn = document.getElementById(`${id}_likes`);
    let likes = parseInt(likeBtn.dataset.likes) + 1;
    likeBtn.dataset.likes = likes;
    likeBtn.innerHTML = HEARTLIKED + ` ${likes}`;

    // change onclick function
    likeBtn.onclick =  () => {
        dislikePost(id)
        return false;
    }
}

export function dislikePost(id) {
    const path = `${id}/dislike`
    fetch(path, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })
    // change quantity of likes
    let likeBtn = document.getElementById(`${id}_likes`);
    let likes = parseInt(likeBtn.dataset.likes) - 1;
    likeBtn.dataset.likes = likes;
    likeBtn.innerHTML = HEART + ` ${likes}`;

     // change onclick function
     likeBtn.onclick =  () => {
        likePost(id)
        return false;
    }
}