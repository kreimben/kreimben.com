import React from 'react';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Layout from '../../components/Layout';

import ReactMarkdown from 'react-markdown/with-html'

export type postPropsType = {content: string }; //, frontmatter: { title: string, date: string }};

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
<<<<<<< Updated upstream
        (filename) => {
            params: {
                slug: filename.replace(".md", "");
            }
        }
    );

=======
        function (filename) {
            return { params : {
                slug: filename.replace(".md", "")
            } }
        }
    );

    // console.log("Paths are " + typeof(paths) + "\n");

>>>>>>> Stashed changes
    return {
        paths,
        fallback: false,
    }
}

<<<<<<< Updated upstream
export async function getStaticProps(props: { slug: string }) {
    const markdownWithMetadata = fs
        .readFileSync(path.join("content/posts", props.slug + ".md")) // props.paths.params.slug
        .toString();
=======
export const getStaticProps = async (props: any) => { //: { params: { slug: string } }) => {
    const markdownWithMetadata = fs.readFileSync(path.join("content/posts", props.slug + ".md")).toString();
>>>>>>> Stashed changes

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

    return {
        props: {
            content: `# ${data.title}\n${content}`,
            frontmatter
        },
    };
}