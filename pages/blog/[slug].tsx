import * as React from 'react';
import Layout from '../../components/Layout';
import { GetServerSideProps, GetServerSidePropsContext, InferGetServerSidePropsType } from 'next'
import getPost, { titleConverter } from '../../model/getPost';
import MDX from '@mdx-js/runtime';

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {

    if (context.req.url) {

        const title = context.req.url;

        try {
            const result = await getPost(title);

            return {
                props: {
                    slug: title,
                    content: result,
                }
            }
        } catch (error) {
            console.log(error);
            return {
                notFound: true,
            }
        }
    } else {
        return {
            notFound: true,
        }
    }
}

const scope = {
    some: 'value'
}

export default function Post(props: InferGetServerSidePropsType<typeof getServerSideProps>) {
    return (
        <Layout title={titleConverter(props.slug)} isHome={false}>
            <article>
                <MDX scope={scope}>
                    {props.content}
                </MDX>
            </article>
        </Layout>
    );
}