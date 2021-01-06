import GhostContentAPI from '@tryghost/content-api';
import APIKey from './APIKey';

const api = new GhostContentAPI({
    url: 'http://193.123.231.139:2368',
    key: APIKey,
    version: 'v3'
})

const getPosts = async () => {

    const posts = await api.posts.browse({ limit: 'all' })
        .then((posts) => {
            return posts;
        })
        .catch(err => console.error(err));

    return posts;
}

const getPost = async (id: string) => {

    const post = await api.posts.read({ id: id })
        .then(post => {
            return post
        })
        .catch(err => console.error(err));

    return post;
}

export { getPosts, getPost };