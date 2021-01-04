import Link from 'next/link';
import { backgroundColor, textColor } from '../styles/globalColorSets'

const elementStyle = "font-extrabold text-xl text-center flex-grow";

const Menu = () => {
    return (
        <nav className="font-black items-center flex py-4 divide-x divide-gray-500 sticky top-0 shadow-lg" style={{backgroundColor:backgroundColor}}>
            <Link href="/"><a className={elementStyle} style={{ color: textColor }}>Home</a></Link>
            <Link href="/blog"><a className={elementStyle} style={{ color: textColor }}>Blog</a></Link>
        </nav>
    )
}

export default Menu;

// TODO: Add search button and actual it's function.