# Ticketless

A system designed to manage event registrations and ticketing for events that lack a dedicated checkout page.

## Potential Users

Ticketless is built for small-scale events that don't have their own dedicated checkout pages, such as college fests, community events, and other informal gatherings.

## Origin of the Idea

The idea for Ticketless came from observing the manual methods used by many small events, especially those hosted by colleges, such as asking attendees to fill out Google Forms and using Excel sheets for check-ins. This approach is inefficient, requires significant manpower, and is prone to errors. Ticketless automates the ticketing and check-in processes, making event management smoother and more efficient.

## Key Features

1. **Ticket Generation with QR Code Support**: Easily generate tickets with QR codes for streamlined check-ins.
2. **QR Scanning via Webcam from Admin Panel**: Scan tickets directly using a webcam for quick verification.
3. **Integration with Payment Gateway (Razorpay)**: Secure payment processing integrated with Razorpay.
4. **Sub-Events Support**: Manage multiple sub-events within a main event seamlessly.
5. **Addon Items Support**: Offer limited-stock items that don't fit the category of sub-events, like merchandise or special passes.
6. **Admin Page with Analytics**: View stats on ticket sales, sub-event sales, addon sales, and total check-ins.
7. **Android App for QR Scanning (Under Development)**: An app will offer faster and more reliable QR scanning than a webcam.
8. **Celery Worker Support**: Handle heavy tasks such as ticket image generation without slowing down the main application.
9. **Webhooks for Payment Monitoring (Razorpay)**: Automatically handle disputes or refunds, disable affected tickets, and send notifications to customers.
10. **Constant Evaluation of Ticket Payment Status**: Monitor all sold tickets to ensure payment success and detect transaction failures, minimizing issues related to late captures. (Razorpay only)

## System Stability

The system is currently under development and testing with "Sabrang 2024" at JK Lakshmipat University. It is not yet ready for live production use but is progressing towards stability.

## Installation

Setting up Ticketless on your local machine is straightforward using Docker:

1. **Install Docker**: Follow the instructions at [Docker Installation](https://docs.docker.com/install/).

2. **Clone the Source Code**:

    ```bash
    git clone https://github.com/Suryansh5545/ticketless.git ticketless && cd ticketless
    ```

3. **Build and Run the Docker Containers**: This may take some time.

    ```bash
    docker compose up --build
    ```

4. **Configure Environment Variables**: Edit `docker.env.example`, rename it to `docker.env`, and configure it to test email support or Razorpay integration.

5. **Access the Application**: Open your browser and navigate to [http://127.0.0.1:4200](http://127.0.0.1:4200). A default superuser account is created:

    - **SUPERUSER**: 
        - **Username**: `admin`
        - **Password**: `password`

## Planned Updates

1. **Additional Payment Gateways**: Integration with Paytm and PhonePe (under development).
2. **Android App**: An Android app is currently under development to enhance QR scanning capabilities.
3. **Test Cases**: Implement test cases for critical functions to ensure reliability.
4. **Organizer User Role**: Allow organizers to add events without admin assistance directly from the frontend.
5. **Support for Multiple Concurrent Events**: Enable hosting of multiple active events on the same site.

## License

This project is licensed under the [MIT License](LICENSE). For more details, see the [LICENSE](LICENSE) file.
