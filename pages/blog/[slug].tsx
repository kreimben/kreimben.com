import React from 'react';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Layout from '../../components/Layout';

import ReactMarkdown from 'react-markdown/with-html'

export type postPropsType = {content: string, frontmatter: { title: string, date: string }};

export default function Post(props: postPropsType) {
    return (
        <Layout>
            <article>
                <ReactMarkdown escapeHtml={false} source={props.content} />
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

export async function getStaticProps(props: { slug: string }) {
    const markdownWithMetadata = fs
        .readFileSync(path.join("content/posts", props.slug + ".md")) // props.paths.params.slug
        .toString();

    const { data, content } = matter(markdownWithMetadata);

    // Convert post data to format: Month day, Year
    const options = { year: "numeric", month: "long", day: "numeric" };
    const date = new Date(data.date);
    const formattedDate = date.toLocaleString("en-US", options);

    const frontmatter = {
        //title: data.title,
        //date: formattedDate,
        ...data,
        date: formattedDate
    };

    alert(frontmatter);

    return {
        props: {
            content: `# ${data.title}\n${content}`,
            frontmatter
        },
    };
}