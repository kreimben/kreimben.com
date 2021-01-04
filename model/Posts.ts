import GhostContentAPI from '@tryghost/content-api';
import APIKey from './APIKey';

const getPosts = async () => {

    const api = new GhostContentAPI({
        url: 'http://localhost:2368',
        key: APIKey,
        version: 'v3'
    })

    const posts = await api.posts.browse({ limit: 'all' })
        .then((posts) => {
            return posts;
        })
        .catch(err => console.error(err));

    return posts;
}

const getPost = async (id: string) => {

    const api = new GhostContentAPI({
        url: 'http://localhost:2368',
        key: APIKey,
        version: 'v3'
    })

    const post = await api.posts.read({ id: id })
        .then(post => {
            return post
        })
        .catch(err => console.error(err));

    return post;
}

export { getPosts, getPost };