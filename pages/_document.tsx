import Document, { Html, Head, Main, NextScript, DocumentContext } from 'next/document'
import Layout from '../components/Layout'

class MyDocument extends Document {
    static async getInitialProps(ctx: DocumentContext) {
        const initialProps = await Document.getInitialProps(ctx)

        return initialProps;
    }
}

export default MyDocument