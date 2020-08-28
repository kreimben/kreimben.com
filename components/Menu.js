import Link from 'next/link';

const elementStyle = "text-red-200";

export default function Menu() {
    return (
        <div className="bg-red-300 items-center flex">
            <Link href="/"><a className={elementStyle}>Home</a></Link>
            <Link href="/aboutme"><a className={elementStyle}>About me</a></Link>
            <Link href="/blog"><a className={elementStyle}>Blog</a></Link>
        </div>
    )
}