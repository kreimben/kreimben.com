import * as React from 'react';
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import Layout from '../../components/Layout';
import { withRouter } from 'next/router'
import ReactMarkdown from 'react-markdown/with-html';
import { GetStaticProps, GetServerSideProps, GetServerSidePropsContext, InferGetServerSidePropsType } from 'next'

/*
export const getStaticPaths: GetStaticPaths = async () => {

    const router = withRouter();
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

    return new Promise< GetStaticPathsResult >(() => {
        return {
            paths,
            fallback: false
        }
    });
}

export const getStaticProps: GetStaticProps = async (props: PropsType ) => {
    const markdownWithMetadata = fs
        .readFileSync(path.join("content/posts", props.paths.slug + ".md"))
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
*/

export const getServerSideProps: GetServerSideProps = async (context: GetServerSidePropsContext) => {

    if (context.params.title) {

        const title = context.params.title;

        alert("title is " + title);

        return {
            props: {
                slug: title,
                isTest: true,
            }
        }

    } else {
        return {
            notFound: true,
        }
    }
}

export default function Post(props: InferGetServerSidePropsType<typeof getServerSideProps>) {
    return (
        <Layout title={ props.slug } isHome={ false }>
            <article>
                {
                    props.isTest === true ?
                        <p>"Pass the test!"</p>
                    :
                        <p>Fail to test!</p>
                }
            </article>
        </Layout>
    );
}