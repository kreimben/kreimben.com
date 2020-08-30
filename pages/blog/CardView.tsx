import Link from 'next/link';

export type blogParams = { title: string, date: string };

export default function CardView(props: blogParams) {
    return (
        <Link href="/">
            <div className="bg-gray-300 w-3/4 text-center py-4 my-4">
                <p className="text-red-600 text-lg" >{props.title}</p>
                <p>{props.date}</p>
            </div>
        </Link>
    );
}