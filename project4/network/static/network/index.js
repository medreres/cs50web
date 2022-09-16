import {loadPosts, clearPosts, create_post} from './helper.js';




document.addEventListener('DOMContentLoaded', () => {

    // load posts from first page
    loadPosts(pageInd, postFilter);

    // create a new post
    document.addEventListener('submit', create_post);

    // // load page with stated index when going back
    // window.onpopstate = function (event) {
    //     clearPosts();
    //     pageInd = event.state['pageInd'];
    //     loadPosts(pageInd, postFilter);
    // }

    // load next page
    document.querySelector('#next_page').addEventListener('click', () => {
        clearPosts();
        loadPosts(++pageInd, postFilter)
    })

    // load prev page
    document.querySelector('#prev_page').addEventListener('click', () => {
        clearPosts();
        loadPosts(--pageInd, postFilter)
    });

});