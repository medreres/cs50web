import {
    loadPosts,
    clearPosts,
    create_post
} from './helper.js';


document.addEventListener('DOMContentLoaded', () => {
    // load posts
    loadPosts(pageInd, postFilter);


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
})

