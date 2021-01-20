import { GetServerSideProps, InferGetServerSidePropsType } from 'next';

import Layout from '../../components/Layout';
import CardView from '../../components/CardView';
import useSWR from 'swr';
import APIKey from '../../model/APIKey';

const index = (props: InferGetServerSidePropsType<typeof getServerSideProps>) => {

    const initialData = props.data;
    const { data, error } = useSWR(`http://193.123.231.139:2368/ghost/api/v3/content/posts/?key=${APIKey}`, fetcher, { initialData });

    if (error) {
        console.error(error);
        alert(error);
        return (
            <Layout title="Kreimben::Error!" isHome={false}>
                <div>
                    Error Occured!
                </div>
            </Layout>
        )
    }

    if (!data) {
        return (
            <Layout title="Kreimben::Loading..." isHome={false}>
                <div>
                    Loading...
                </div>
            </Layout>
        )
    }

    return (
        <Layout title="Kreimben::Blog" isHome={false}>
            <div className="flex flex-wrap mt-8 mb-8 justify-center">
                {
                data.posts.map(
                    (post) => {
                        return (
                            <CardView title={post.title} date={post.created_at} id={post.id} slug={post.slug} key={`${post.title}-${post.created_at}`} />
                        );
                    }
                )
                }
            </div>
        </Layout>
    )
}

export default index;

const fetcher = async () => {
    const res = await fetch(`http://193.123.231.139:2368/ghost/api/v3/content/posts/?key=${APIKey}`);
    const json = await res.json();

    return json;
}

export const getServerSideProps: GetServerSideProps= async () => {

    const data = await fetcher();

    return { props: { data } };
}