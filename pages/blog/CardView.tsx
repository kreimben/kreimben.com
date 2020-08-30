import Link from 'next/link';

export type blogParams = { title: string, date: string };

export default function CardView(props: blogParams) {
    return (
        <Link href="/">
            <div className="bg-gray-500 w-2/3" >
                <p className="text-red-700 text-lg" >{props.title}</p>
                <p>{props.date}</p>
            </div>
        </Link>
    );
}