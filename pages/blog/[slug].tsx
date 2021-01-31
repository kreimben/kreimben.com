import * as React from 'react';
import { GetServerSideProps, GetServerSidePropsContext, InferGetServerSidePropsType } from 'next'

import Layout from '../../components/Layout';
import DateParser from '../../model/DateParser';
import APIKey from '../../model/APIKey';
import useSWR from 'swr';

const url = (id: string) => {
    return `http://193.123.231.139:2368/ghost/api/v3/content/posts/${id}/?key=${APIKey}`;
}

const fetcher = async (id: string) => {

    //console.log("Id as parameter is: " + id);

    const res = await fetch(url(id));
    const json = await res.json();

    //console.log("result json is: " + json);

    return json;
}

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {

    const id = context.query.slug.toString();

    console.log("id is: " + id);
    const data = await fetcher(id);

    return { props: { data, id } };
}

export default function Post(props: InferGetServerSidePropsType<typeof getServerSideProps>) {

    const initialData = props.data;

    const URL = url(props.id);

    const { data } = useSWR(URL, fetcher, { initialData: initialData, revalidateOnFocus: false });

    console.log(`Requesting URL is: ${URL}`);
    console.log(data.posts[0].created_at);
    const result = DateParser(data.posts[0].created_at);

    return (
        <Layout title="Kreimben::blog" isHome={false}>
            <div className="flex justify-center pt-12">
                <div className="w-3/5 shadow-2xl py-6 text-center bg-indigo-400 rounded-2xl font-black text-4xl select-none">{data.posts[0].title}</div>
            </div>

            <div className="flex justify-center pt-6">
                <div className="shadow-2xl py-3 px-4 text-right bg-purple-400 rounded-2xl font-bold text-lg select-none">
                    written in {result[0]}  {result[1]}
                </div>
            </div>

            <div className="pt-6 pb-12 flex justify-center">
                <div className="w-3/5 shadow-2xl px-8 py-8 bg-blue-300 rounded-2xl font-serif text-lg select-none leading-loose" dangerouslySetInnerHTML={{ __html: data.posts[0].html }} />
            </div>
        </Layout>
    );
}