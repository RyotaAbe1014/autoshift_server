from sqlalchemy.orm import Session
from models.organization import Organization as OrganizationModel
import schemas.organization as OrganizationSchema
from auth.hash import Hash


def create_organization(db: Session, organization_create: OrganizationSchema.OrganizationCreate) -> OrganizationModel:
    organization = OrganizationModel(
        name=organization_create.name,
        password=Hash.get_password_hash(organization_create.password))
    db.add(organization)
    db.commit()
    db.refresh(organization)
    return organization


def get_organization_id(db: Session, organization_name: str) -> int:
    organization = db.query(OrganizationModel).filter(OrganizationModel.name == organization_name).first()
    return organization.id