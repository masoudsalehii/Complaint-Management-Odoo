FROM odoo:15

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory within the container
WORKDIR /mnt/extra-addons

# Copy custom addons from the local system to the container
COPY ./addons/* /mnt/extra-addons/

# Switch back to the working directory of Odoo
WORKDIR /mnt/odoo

# Expose Odoo port
EXPOSE 8069

# Start Odoo
CMD ["odoo", "--addons-path=/mnt/odoo/addons,/mnt/extra-addons"]
