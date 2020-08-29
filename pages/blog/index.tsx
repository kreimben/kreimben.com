import Layout from '../../components/Layout'
import CardView from '.'

import fs from 'fs'
import matter from 'gray-matter'

export default function index({ posts }) {
    return (
        <Layout title="Kreimben::Blog">
            <h1>This is my blog</h1>
            {
                posts.map(
                    ({ frontmatter: { title, date } }) => {
                        <CardView title={title} date={date} />
                    }
                )
            }

            <CardView title="this is sample title" date={Date()} />
        </Layout>
    )
}

export async function getStaticProps() {

    const files = fs.readdirSync(`${process.cwd()}/content/posts`);

    const posts = files.map(
        (filename) => {

            const markdownWithMetadata = fs.readFileSync(`content/posts/${filename}`).toString();

            const { data } = matter(markdownWithMetadata);

            const options = { year: "numeric", month: "long", day: "numeric" };
            const date = new Date(data.date);
            const formattedDate = date.toLocaleString("en-US", options);

            const frontmatter = {
                ...data,
                date: formattedDate
            };

            return {
                slug: filename.replace(".md", ""),
                frontmatter,
            }; // this object is going to be `posts`.
        }
    );

    return {
        props: {
            posts,
        },
    };
}