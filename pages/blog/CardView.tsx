import Link from 'next/link';
import DateParser from './DateParser';

export type blogParams = { title: string, date: string, id: string, slug: string };

export default function CardView(props: blogParams) {
    return (
        <Link href='/blog/[slug]' as={`/blog/${props.id}`}>
            <div className="bg-gray-300 w-1/4 items-center text-center py-12 m-4 rounded-lg shadow-xl">
                <p className="text-black hover:text-gray-600 mx-4 font-bold text-2xl">{props.title}</p>
                <DateWrapper date={props.date} />
            </div>
        </Link>
    );
}

function DateWrapper(props: { date: string }) {

    const result = DateParser(props.date);

    return (
        <div className="rounded-lg bg-blue-300 inline-block mt-4" key={props.date}>
            <p className="text-blue-500 px-2 text-xs">{result[0]}  {result[1]}</p>
        </div>
    );
}