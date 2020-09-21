import React from 'react';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Layout from '../../components/Layout';

import ReactMarkdown from 'react-markdown/with-html'

export default function Post(props: { title: string, date: string, content: string } ) {
    return (
        <Layout>
            <article>

            </article>
        </Layout>
    );
}

export async function getStaticPaths() {
    const files = fs.readdirSync("content/posts");

    const paths = files.map(
        (filename) => {
            params: {
                slug: filename.replace(".md", "");
            }
        }
    );

    return {
        paths,
        fallback: false,
    }
}

type propsType = { paths: { params: { slug: string } } };
export async function getStaticProps(props: propsType) {
    const markdownWithMetadata = fs
    .readFileSync(path.join("content/posts", props.paths.params.slug + ".md"))
    .toString();

    const { data, content } = matter(markdownWithMetadata);

    // Convert post data to format: Month day, Year
    const options = { year: "numeric", month: "long", day: "numeric" };
    const date = new Date(data.date);
    const formattedDate = date.toLocaleString("en-US", options);

    const frontmatter = {
        title: data.title,
        date: formattedDate,
        content: data.content
    };

    return (
        props: {
            content: `${data.title} ${content}`,
            frontmatter: { title: string, date: string, content: string },
        },
    );
}