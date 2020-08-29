import Link from 'next/link';

export type blogParams = { title: string, date: string };

let newdate = new Date();

export default function CardView(props: blogParams) {
    return (
        <Link href="/">
            <div className="bg-gray-500" >
                <p className="text-red-700 text-lg" >{props.title}</p>
                <p>{props.date}</p>
            </div>
        </Link>
    );
}