import React from 'react';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Layout from '../../components/Layout';
import { useRouter } from 'next/router';

import ReactMarkdown from 'react-markdown/with-html'
// import { GetStaticProps, InferGetStaticPropsType, GetStaticPaths } from 'next'

type PostType = {
    content: string,
    frontmatter: {
        title: string,
        date: string
    }
};

export const getStaticPaths = async () => {
    const router = useRouter();
    const uri = router.asPath;
    alert(uri);

    let files = fs.readdirSync("content/posts");
    console.log("\nDate: " + Date().toString() + "\n");
    files = files.filter((name) => name !== ".DS_Store");
    console.log("Files are " + files + "\n");

    const paths = files.map(
        function (filename) {
            params: {
                slug: filename.replace(".md", "");
            }
            //filename.replace(".md", "") as string;
        }
    );

    console.log("Paths are " + typeof(paths) + "\n");

    return {
        paths,
        fallback: false,
    }
}

export const getStaticProps = async (props: any) => { //: { params: { slug: string } }) => {
    const markdownWithMetadata = fs
        .readFileSync(path.join("content/posts", props.slug + ".md"))
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

    console.log("type of content is " + content);

    return {
        props: {
            content: `# ${data.title}\n${content}`,
            frontmatter
        } as PostType,
        //revalidate: 1,
    };
}

export default function Post(props: PostType ) {
    return (
        <Layout title={ props.frontmatter.title } isHome={ false }>
            <article>
                <ReactMarkdown escapeHtml={false} source={props.content} />
            </article>
        </Layout>
    );
}