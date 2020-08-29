import Link from 'next/link';

type blogParams = { title: string, date: Date };

const CardView: React.FunctionComponent<blogParams> = ({ title, date }) => (
    <Link href="/">
        <div className="bg-gray-500" >
            <p className="text-red-700 text-lg" >{title}</p>
            <p>{date}</p>
        </div>
    </Link>
);