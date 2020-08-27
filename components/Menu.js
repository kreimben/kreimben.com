import Link from 'next/link';

export default function Menu() {
    return (
        <div>
            <Link href="/"><a>Home</a></Link>
            <Link href="/aboutme"><a>About me</a></Link>
            <Link href="/blog"><a>Blog</a></Link>
        </div>
    )
}