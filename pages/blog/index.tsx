import { GetStaticProps } from 'next';

import Layout from '../../components/Layout';
import CardView from './CardView';
import { getPosts } from '../../model/Posts';

export default function index(props: any) {
    return (
        <Layout title="Kreimben::Blog" isHome={false}>
            <div className="flex flex-wrap mt-8 mb-8 justify-center">
                {props.posts.map(
                    (post) => {
                        return (
                            <CardView title={post.title} date={post.created_at} id={post.id} slug={post.slug} key={`${post.title}-${post.created_at}`} />
                        );
                    }
                )}
            </div>
        </Layout>
    )
}

export const getStaticProps: GetStaticProps = async () => {

    const posts = await getPosts();

    return {
        props: { posts },
    };
}