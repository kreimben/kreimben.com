import * as React from 'react';
import { GetServerSideProps, GetServerSidePropsContext, InferGetServerSidePropsType } from 'next'

import { getPost } from '../../model/Posts';
import Layout from '../../components/Layout';
import DateParser from '../../model/DateParser';

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

    const result = DateParser(props.result.created_at);

    return (
        <Layout title="Kreimben::blog" isHome={false}>
            <div className="flex justify-center pt-12">
                <div className="w-3/5 shadow-2xl py-6 text-center bg-indigo-400 rounded-2xl font-black text-4xl select-none">{props.result.title}</div>
            </div>

            <div className="flex justify-center pt-6">
                <div className="shadow-2xl py-3 px-4 text-right bg-purple-400 rounded-2xl font-bold text-lg select-none">
                    written in {result[0]}  {result[1]}
                </div>
            </div>

            <div className="pt-6 pb-12 flex justify-center">
                <div className="w-3/5 shadow-2xl px-8 py-8 bg-blue-300 rounded-2xl font-serif text-lg select-none leading-loose" dangerouslySetInnerHTML={{ __html: props.result.html }} />
            </div>
        </Layout>
    );
}