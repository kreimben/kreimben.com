import Link from 'next/link';

export type blogParams = { title: string, date: string, as: string };

export default function CardView(props: blogParams) {
    return (
        <Link href="./[slug]" as={`./${props.as}`}>
            <div className="bg-gray-300 w-1/4 items-center text-center py-12 m-4 rounded-lg shadow-xl">
                <p className="text-black hover:text-gray-600 mx-4 capitalize font-bold text-2xl">{props.title}</p>
                <DateWrapper date={props.date} />
            </div>
        </Link>
    );
}

function DateWrapper(props: { date: string }) {
    return (
        <div className="rounded-lg bg-blue-300 inline-block mt-4">
            <p className="text-blue-500 px-2 text-xs">{props.date}</p>
        </div>
    );
}