from email_reply_parser import EmailMessage


class NHSNETEmailReplyParser(object):
    """ Represents a email message that is parsed from an nhs.net email address.
    """

    @staticmethod
    def read(text):
        """ Factory method that splits email into list of fragments

            text - A string email body

            Returns an NHSNETEmailMessage instance
        """
        return NHSNETEmailMessage(text).read()

    @staticmethod
    def parse_reply(text):
        """ Provides the reply portion of email.

            text - A string email body

            Returns reply body message
        """
        return NHSNETEmailMessage.read(text).reply


class NHSNETEmailMessage(EmailMessage):
    """
    Emails from nhs.net don't include traditional quoting for the original
    message in a thread, instead they include a block of formatted text like:

        From: Company Name [mailto:address@domain.com]
        Sent: 29 March 2013 13:44
        To: recipient one (number one); recipient two (number two)
        Subject: Email subject

    We search for this block (specifically the words at the start of the lines)
    and treat everything after this block as quoted.
    """
    MULTI_QUOTE_HDR_REGEX = r'(On\s.*?wrote:|From:\s.*?Sent:\s.*?To:\s.*?Subject:\s.*?\Z)'
    QUOTED_REGEX = r'(>+)|(From:\s.*?Sent:\s.*?To:\s.*?Subject:\s.*?)'
