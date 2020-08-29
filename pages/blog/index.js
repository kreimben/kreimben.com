import Layout from '../../components/Layout'
import CardView from './cardview'

import fs from 'fs'
import matter from 'gray-matter'

export default function index({ posts }) {
    return (
        <Layout title="Kreimben::Blog">
            <h1>This is my blog</h1>
            {
                posts.map(
                    ( { frontmatter: { title, date } } ) => {
                        console.log("Title: ", title, "and Date: ", date);
                        <CardView title={title} date={date} />
                    }
                )
            }
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