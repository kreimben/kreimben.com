import Layout from '../../components/Layout'
import CardView from './CardView'

import fs from 'fs'
import matter from 'gray-matter'

type postsParams = { posts: [{ slug: string, frontmatter: { title: string, date: string } }] };
type frontmatterParams = {

}

export default function index({ posts }: postsParams) {
    return (
        <Layout title="Kreimben::Blog">
            <p className="text-lg text-red-600">This is my blog</p>
            {
                posts.map(
                    ({ frontmatter: { title, date } } ) => {
                        <CardView title={title} date={date} />
                    }
                )
            }
            <br />
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

            const title = data.title;
            console.log(title);

            const frontmatter = {
                title: title as string,
                date: formattedDate
            };

            return {
                slug: filename.replace(".md", ""),
                frontmatter,
            }; // this object is going to be `posts`.
        }
    );

    console.log(typeof posts);
    console.log(posts);

    return {
        props: {
            posts,
        },
    };
}