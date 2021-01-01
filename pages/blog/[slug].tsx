import * as React from 'react';
import { GetServerSideProps, GetServerSidePropsContext, InferGetServerSidePropsType } from 'next'

import PostLayout from './Post/PostLayout';
import { getPost } from '../../model/Posts';
import Layout from '../../components/Layout';

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {

    const id = context.query.slug.toString();

    const result = await getPost(id);

    return {
        props: {
            result,
        },
    };
}

export default function Post(props: InferGetServerSidePropsType<typeof getServerSideProps>) {
    return (
        <Layout title="Kreimben::blog" isHome={false}>
            <PostLayout props={props.result} />
            <div className="bg-blue-500">
                {props.result.html}
            </div>
        </Layout>
    );
}