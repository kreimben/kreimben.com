import Link from 'next/link';

const elementStyle = "text-blue-800 font-extrabold text-xl text-center flex-grow hover:text-blue-600";

const Menu = () => {
    return (
        <nav className="bg-gray-300 items-center flex py-4 divide-x divide-gray-500 sticky top-0 shadow-lg">
            <Link href="/"><a className={elementStyle}>Home</a></Link>
            <Link href="/blog"><a className={elementStyle}>Blog</a></Link>
        </nav>
    )
}

export default Menu;

// TODO: Add search button and actual it's function.