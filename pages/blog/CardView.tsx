import Link from 'next/link';

export type blogParams = { title: string, date: string };

export default function CardView(props: blogParams) {
    return (
        <Link href="/">
            <div className="bg-gray-300 w-1/3 text-center py-4 m-4 rounded-lg">
                <p className="text-red-700 hover:text-red-400 text-lg" >{props.title}</p>
                <p>{props.date}</p>
            </div>
        </Link>
    );
}