import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> { props.title } </title>
            </Head>
            <Menu />
            <main>
                { props.children }
            </main>
        </div>
    )
}