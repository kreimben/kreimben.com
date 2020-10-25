import fs from 'fs'
import matter from 'gray-matter'
import Link from 'next/link'

import Layout from '../../components/Layout'
import CardView from './CardView'

type postsParams = { posts: [{ slug: string, frontmatter: { title: string, date: string } }] };

export default function index({ posts }: postsParams) {
    return (
        <Layout title="Kreimben::Blog" isHome={false}>
            <div className="flex flex-wrap mt-8 mb-8 justify-center">
                {posts.map(
                    ({ frontmatter: { title, date }, slug }) => {
                        if (title !== null) {
                            return (
                                <CardView title={title} date={date} slug={slug} />
                            );
                        }
                    }
                )}
            </div>
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
                title: data.title as string,
                date: formattedDate
            };

            if (filename === ".DS_Store") {
                return {
                    slug: null,
                    frontmatter: {
                        title: null,
                        date: null
                    }
                };
            } else {
                return {
                    slug: filename.replace(".md", ""),
                    frontmatter,
                }; // this object is going to be `posts`.
            }
        }
    );

    // console.log(posts);

    return {
        props: {
            posts,
        },
    };
}